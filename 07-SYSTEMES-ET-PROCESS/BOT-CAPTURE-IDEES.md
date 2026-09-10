# 🤖 Bot de capture d'idées @Prodaicontentbot → Notion

**Créé le 19 août 2026 · ACTIF depuis le 19 août 2026, 19 h**
Workflow n8n : [@Prodaicontentbot](https://nevada.app.n8n.cloud/workflow/ywOK5MMBPGfXnCgv) (`ywOK5MMBPGfXnCgv`)
Base Notion : [Neva Content — Pipeline éditorial](https://app.notion.com/p/3987299b223480428ab6e470cc6bd8ea)

---

## 1. À quoi ça sert

Tu dictes une note vocale (ou tu écris) au bot Telegram **@Prodaicontentbot**.
Quinze secondes plus tard, une **ligne de travail complète** existe dans ton pipeline éditorial Notion — pas un vrac d'idée, une fiche exploitable.

L'objectif n'est pas de « stocker des idées ». C'est que **l'idée arrive déjà qualifiée**, pour que ton pool d'idées devienne une vraie file d'attente de production.

---

## 2. Ce que le bot remplit tout seul

| Colonne Notion | Ce que l'IA produit |
|---|---|
| **Sujet** (titre) | Le sujet reformulé proprement, 90 caractères max |
| **Hook** | Une accroche en une phrase, qui doit tenir sans le son |
| **Pilier** | Product Builder · IA appliquée · Business & Mindset · Cas réels |
| **Catégorie** | Difficulté d'intégration · Insights · Tips d'intégration |
| **Plateforme** | LinkedIn ou Instagram |
| **Format** / **Format Instagram** / **Format LinkedIn** | Le format le plus adapté |
| **Instagram** | L'angle Instagram (point A → bascule → point B) |
| **LinkedIn** | L'angle LinkedIn (expérience vécue → méthode → enseignement) |
| **CTA** | Une seule action demandée |
| **Lead Magnet** | L'actif gratuit qui accomplit la prochaine tâche du lecteur |

Et il pose automatiquement :
- ~~**Phase éditoriale = Quarantaine**~~ ⚠️ **OBSOLÈTE au 28/08** : la propriété `Phase éditoriale` a été supprimée de la base lors de sa restructuration autour du funnel 27 €. Si le nœud n8n l'écrit encore, il échoue. → **Vérifier le workflow et router les captures vers la vue _04 — BANQUE D'IDÉES · HORS FUNNEL_** (les lignes sans `Project 1` y tombent automatiquement)
- **Statut = Idée capturée**
- **Le verbatim complet** (ta transcription mot à mot, datée) dans le **corps de la page** — rien n'est perdu

L'IA ne peut choisir **que des options qui existent déjà** dans ta base : impossible qu'elle invente une catégorie et casse tes vues.

---

## 3. Le chemin, étape par étape

```
Message Telegram
   ↓
Voix, texte, ou autre ?
   ├── 🎙️ Note vocale → récupération du fichier → transcription Whisper (français)
   ├── ✍️ Message texte (qui ne commence PAS par « / ») → directement
   └── 📎 Commande (/start…), photo, sticker → message d'accueil, aucune ligne créée
   ↓
Normalisation (un seul texte propre)
   ↓
🚦 Garde-fou : transcription exploitable ?
   └── Moins de 15 caractères, ou artefact Whisper → « Je n'ai rien entendu », aucune ligne créée
   ↓
Qualification éditoriale par l'IA (gpt-5.4, avec le canon Neva en consigne)
   ↓
Création de la ligne Notion (+ emoji 💡 sur la page)
   ↓
✅ Confirmation Telegram avec le résumé + le lien vers la page
   └── ⚠️ Si Notion échoue : le bot renvoie le verbatim pour que rien ne soit perdu
```

17 nœuds, projet personnel n8n.

---

## 4. Credentials branchés

| Nœud | Credential |
|---|---|
| Bot Telegram · Recuperer le fichier audio · Confirmer sur Telegram · Signaler une erreur · Repondre format non supporte | **Telegram account 3** (à renommer `Telegram — Prodaicontentbot`) |
| Transcrire la voix · Modele IA | **OpenAI account** |
| Creer la ligne Notion | **Notion account** |
| Rien entendu | **Telegram account 3** |

---

## 5. Journal des corrections

**19/08, 19 h — trois défauts trouvés au premier test**
1. **Rien ne s'enregistrait** : le workflow n'avait jamais été publié (`active: false`, 0 exécution). Telegram recevait bien les messages, personne n'écoutait. → **Publié.**
2. **`/start` créait une ligne parasite** : la commande était traitée comme une idée et aurait généré un sujet « start » dans Notion. → Les messages commençant par `/` partent maintenant sur la branche d'accueil.
3. **Le message d'accueil** était un refus sec. → Remplacé par une vraie explication de ce que le bot sait faire.

**19/08, 20 h — garde-fou anti-silence**
Une note vocale d'une seconde (donc du silence) avait produit la ligne `IDEA-57`. Whisper, sur un audio vide, recrache un artefact appris à l'entraînement : « Sous-titres réalisés par la communauté d'Amara.org ». L'IA a ensuite fait consciencieusement une fiche complète à partir de cette phrase.
→ Nouveau nœud **Transcription exploitable** : rejette les messages de moins de 15 caractères et les artefacts connus (`amara.org`, `sous-titr`, `soustitreur`, « merci d'avoir regardé », « abonnez-vous »). Le bot répond alors « 🙉 Je n'ai rien entendu, dis-moi ça » et n'écrit rien dans Notion.
⚠️ Leçon générale : **une transcription non vide ne veut pas dire une transcription réelle.** Tout pipeline voix → base de données a besoin de ce filtre.

**19/08 — vues Notion**
Les vues *00 — Sujets à approuver*, *Instagram — Production* et *LinkedIn — Production* ont été supprimées à la main (le connecteur Notion n'expose aucune commande de suppression de vue).

**19/08 — changement de destination**
La vue *00 — Sujets à approuver* est supprimée du tableau. Les idées atterrissent désormais en **Quarantaine**, dans *02 — Pool d'idées / Quarantaine*.

---

## 5 bis. ⚠️ Bug confirmé le 28/08 — le verbatim russe est traduit avant d'être stocké

**Symptôme :** Katerina dicte en russe. Dans Notion, le corps de page contient un texte **français**, et il faut réécouter la note vocale d'origine pour retrouver l'idée réelle.

**Preuve —** fiche `IDEA-60` du 21/08 à 10:24. Corps de page enregistré :

> « Dès que l'apprentissage technique arrive, il faut l'adapter à son **niveau d'actualité**. […] Il faut également changer **son mentalité** au niveau d'actualité afin de créer un réflexe. »

Ce n'est pas du français écrit par une francophone : c'est du russe traduit littéralement (`уровень актуальности` → « niveau d'actualité »). **Le verbatim original n'a jamais été stocké.**

**Cause —** le nœud *Transcrire la voix* force `language: fr`. Whisper, à qui l'on impose une langue de sortie différente de la langue parlée, ne transcrit pas : il **traduit**. Le verbatim est donc déjà perdu à l'étape 1, avant même que le LLM intervienne.

### Les deux corrections

**1. Nœud `Transcrire la voix` — laisser la langue en détection automatique**

| Paramètre | Avant | Après |
|---|---|---|
| `language` | `fr` (forcé) | **vide** (auto-détection) |

Whisper transcrit alors le russe en russe, mot pour mot. Katerina alternant FR et RU, l'auto-détection vaut mieux que `ru` en dur.

**2. Nœud `Modele IA` — interdire explicitement de toucher au verbatim**

Ajouter cette règle en tête du prompt système :

```
RÈGLE ABSOLUE — LE VERBATIM EST INTOUCHABLE.
Le champ `verbatim` reçoit la transcription EXACTEMENT telle qu'elle arrive :
même langue, mêmes mots, même ordre, mêmes répétitions et hésitations.
Interdit : traduire, corriger la grammaire, reformuler, résumer, « améliorer ».
Si la transcription est en russe, le verbatim reste en russe.

Les champs éditoriaux (Sujet, Hook, Instagram, LinkedIn, CTA) peuvent
être rédigés en français. Le verbatim, jamais.
```

Et dans le corps de page créé, séparer clairement les deux blocs :

```
## 🎙️ Verbatim original — <langue détectée>
<transcription brute, intouchée>

## ✍️ Reformulation éditoriale (générée)
<le reste>
```

**Pourquoi ça compte :** le Tone of Voice repose sur les formulations réelles de Katerina (`04-TONE-OF-VOICE-KATERINA-NEVA.md` §1 : « entrer par une scène », les tournures personnelles à préserver). Un verbatim traduit détruit exactement la matière que le TOV cherche à protéger.

---

## 6. Points de vigilance n8n (appris ici)

- **Publier ≠ tester.** « Execute workflow » n'écoute qu'UN message puis s'arrête. Pour du 24 h/24 il faut **Publish**. En mode actif, les exécutions ne s'allument plus sur le canevas : elles sont dans l'onglet **Executions**.
- Détacher un credential dans l'éditeur laisse le nœud **sans credential** — il faut en rattacher un, sinon le nœud échoue silencieusement à l'activation.

---

## 7. Extension à construire — développer une idée sans ouvrir Notion

**Le problème réel :** capturer marche depuis le téléphone. **Développer, non** — parce qu'il faut désigner quelle idée, donc voir le tableau, donc être devant un écran. Le tableau devient le goulot.

**Le principe :** ce n'est pas à Katerina d'aller chercher l'idée dans Notion. C'est au bot de lui présenter ses idées et de recevoir sa décision, dans Telegram.

### A. Boutons sur la confirmation de capture *(le plus important)*

Aujourd'hui le bot confirme par un texte + un lien Notion. Ajouter un **clavier inline** sous la confirmation :

```
💡 Idée captée — « Apprendre une compétence ne suffit pas… »

[ ✍️ Développer ]  [ ✅ Garder telle quelle ]  [ 🗑 Jeter ]
```

Katerina vient de dicter : l'idée est fraîche, elle est déjà dans la conversation. **Un tap suffit, aucun identifiant à connaître, aucun tableau à ouvrir.**

*Nœud n8n :* `Telegram → Send Message` avec `replyMarkup: inlineKeyboard`, chaque bouton portant `callback_data = develop:<page_id>`. Un second trigger `Telegram Trigger` sur `callback_query` reçoit le tap.

### B. Commande `/liste` — reprendre une idée ancienne

```
/liste
→ 🗂 5 idées en attente :
   1. Apprendre une compétence…        (21/08)
   2. Я люблю своих конкурентов          (20/08)
   3. Codex vs Claude Code…              (19/08)
   [ 1 ]  [ 2 ]  [ 3 ]  [ 4 ]  [ 5 ]
```

Filtre : `Statut = Idée capturée` **et** `Unité mère` vide, trié par `Date de capture` décroissante, limité à 5. Un tap sur le numéro lance le développement.

### C. Rappel du lundi

Chaque lundi matin, le bot envoie les idées non développées de la semaine, avec les mêmes boutons. Rien ne se perd par oubli.

### D. Ce que fait « Développer »

Le workflow lit la fiche Notion (verbatim inclus), passe la chaîne de rédaction (`PIPELINE-REDACTION-POST.md`), remplit `Pain`, `Solution`, `Hook`, `Instagram`, `LinkedIn`, `CTA`, `Lead Magnet`, puis passe `Statut → Rédigé` et renvoie un résumé dans Telegram.

> ⚠️ **Limite à assumer.** Un nœud LLM dans n8n produit un **bon premier jet**, pas le travail complet : la chaîne en 6 étapes mobilise des agents spécialisés qui n'existent que dans une vraie session. Le partage réaliste :
>
> | Où | Quoi |
> |---|---|
> | Téléphone, en mobilité | capture · tri · **premier jet** |
> | Session Claude, au bureau | chaîne complète · Tone of Voice · validation |
>
> L'intérêt n'est pas de supprimer le travail au bureau : c'est que **l'idée soit déjà dégrossie** quand Katerina s'y met, au lieu de repartir d'une note vocale brute.

### Ordre de construction

1. **Corriger la transcription russe** (§5 bis) — un premier jet bâti sur un verbatim traduit part déjà de travers.
2. Boutons sur la confirmation (A) — c'est 80 % du gain.
3. Commande `/liste` (B).
4. Rappel du lundi (C).

---

## 8. Autres idées d'extension (plus tard)

- **Commande `/vrac`** : capturer sans qualification IA, pour les idées à peine formulées.
- **Photo d'écran → idée** : envoyer une capture de post inspirant, l'IA en extrait l'angle transposé.
- **Retour hebdo** : chaque lundi, le bot envoie les idées en attente de tri.
- **Boutons Telegram** : ✅ Approuver / ♻️ Reformuler / 🗑 Jeter directement depuis la confirmation, pour faire passer la ligne de Quarantaine à *Sujet approuvé* sans ouvrir Notion.
