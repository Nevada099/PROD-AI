# Architecture d'offre — 3 couches : OPERATE · ATTRACT · INTERACT
*Reformulation de l'offre intégrant la **couche IA générative de contenu** comme moteur autonome. Complète `SEPARATION-LAB-ACADEMY.md` (la règle Lab/Academy reste) et relie les systèmes déjà documentés. Soumis à la règle de preuve du cockpit (source · statut · limite).*
*Créé le 27/08/2026.*

> ✅ **VALIDÉ par Katerina le 27/08/2026** — c'est la **structure d'offre canonique** du Lab. Remplace la v2 `04-OFFRES-REPACKAGEES.md` (conservée comme historique). Refonte propagée dans : `SEPARATION-LAB-ACADEMY.md`, `02-PALETTE-SERVICES-MAX.md`, `PRODAI-MASTER-MAP.md`, `00-COCKPIT.md`.

---

## 0. Ce qui change (analyse vs l'existant)
La couche **contenu génératif** était éclatée dans le dossier : production vidéo IA (offre), mini-séries (offre), « moteur de contenu » mêlé à l'automatisation. On la **sort comme moteur autonome** et on range les capacités du Lab en **3 couches** :

| Capacité (source : `SEPARATION-LAB-ACADEMY.md`) | Couche v3 |
|---|---|
| Automatisation sur mesure *(PILOTE — Booking, JobsAI)* | **OPERATE** |
| Production vidéo IA *(TESTÉ/PILOTE — Bouygues, Emerige)* + Mini-séries *(PILOTE — Jean-Pierre)* | **ATTRACT** |
| Live Avatar métier *(PILOTE — Jade/Collection Privée)* | **INTERACT** |
| Concept Business 0→1 *(HYPOTHÈSE — Bubble/Laverie)* | offre méta transverse |

**Règle d'or ajoutée : ne jamais mélanger les 2 usages de l'avatar** (voir §2). *(Cohérent avec l'arbitrage cockpit n°4 : Neva a un mode génératif ET un mode agentique.)*

---

## 1. Le modèle en 3 couches
```
┌───────────────────────────────────────────────┐
│ 1 · OPERATE   — AI Broker / CRM OS             │ système INTERNE (faire tourner)
│   qualification · CRM · tâches · matching       │   → dossier 07-SYSTEMES-ET-PROCESS
│   estimation · suivi · réponses                 │
├───────────────────────────────────────────────┤
│ 2 · ATTRACT   — AI Content Factory  ⭐          │ ATTIRER (contenu génératif)
│   scripts · reels · avatars scriptés · visuels  │   → dossier 05-MARQUE-ET-CONTENU
│   property videos · social media                │   ⭐ vendable SEULE
├───────────────────────────────────────────────┤
│ 3 · INTERACT  — Avatar / Chat Front Office      │ CONVERTIR (conversation live)
│   site · chat · qualification · live avatar     │   → Live Avatar métier (Jade)
│   lead capture                                  │
└───────────────────────────────────────────────┘
```
Vertical immo (le wedge) = **Real Estate AI OS**. Le même modèle se réplique sur d'autres secteurs (générique : *AI Operating System · AI Content System · AI Interactive Front Office*).

---

## 2. Les 3 familles d'IA/avatars + les 2 usages (distinction fondamentale)
| Famille | Ce que c'est | Couche | Statut |
|---|---|---|---|
| **1. Avatar conversationnel / interactif** | Neva/Jade live, branchée LLM + outils + CRM ; répond, qualifie, propose, crée une demande de visite | **INTERACT** | PILOTE (Jade) |
| **2. Avatar média / contenu** | Vidéo où l'avatar présente un bien / explique ; **ne répond pas, ne lit pas le CRM** ; préfabriqué | **ATTRACT** | à faire exister (passeport Neva) |
| **3. Génération visuelle immo** | Photo→vidéo, camera move, satellite→quartier→immeuble, carrousel, teaser | **ATTRACT** | TESTÉ (portfolio) |

> ⚠️ **Usage 1 — l'avatar qui RÉPOND** (live, LLM+CRM+outils) = INTERACT.
> **Usage 2 — l'avatar qui ATTIRE** (vidéo scriptée, pré-enregistrée, zéro CRM) = ATTRACT.
> *Décision de lancement (cockpit arbitrage 5) : Neva = **média seul** d'abord → donc on démarre par l'usage 2.*

---

## 3. Les 4 briques commerciales *(chacune vendable seule, combinables)*
1. **AI Broker OS — Core** *(OPERATE)* : intake leads · qualification acheteur/vendeur · dictée→fiche · suivi · tâches · réponses préparées · CRM substitut ou connecté · validation humaine. *(PILOTE)*
2. **AI Broker OS — Market** *(OPERATE +marché)* : DVF & sources · comparables · estimation assistée · avis de valeur · synthèse marché · aide au mandat. *(HYPOTHÈSE — data à brancher)*
3. **AI Content Factory** *(ATTRACT)* ⭐ : scripts · calendrier · vidéos avatar scriptées · reels · **photos→vidéo** · posts experts · stories · captions · CTA, par cible (vendeur/acquéreur/propriétaire/investisseur). **Se vend sans CRM, sans Apimo, sans live avatar.** *(TESTÉ/PILOTE)*
4. **AI Front Office Interactive** *(INTERACT, premium)* : chat site · qualification visiteur · **avatar live** · orientation · récupération lead · pré-qualif avant RDV. *(PILOTE)*

*Prix : ouverts (arbitrage prix non tranché — ne pas présenter comme acquis).*

---

## 4. Les 3 niveaux de packaging
| Niveau | Contenu | Couches |
|---|---|---|
| **1 — Contenu seul** | ex. 4 reels/mois · 8 stories · 2 avatars experts · 1 vidéo quartier · 1 teasing | ATTRACT |
| **2 — Contenu + Operating** | + qualification · CRM · tâches · pipeline interne | ATTRACT + OPERATE |
| **3 — + Front Office** | + chat site · live avatar · lead en direct | les 3 |

---

## 5. Pipeline `Property Content Factory` (la brique ATTRACT)
**Entrées** : photos · descriptif · infos bien · cible · quartier · angle · persona/ton · format.
```
INPUT
 ↓ 1. Ingestion du bien (adresse, surface, pièces, atouts, prix, quartier, photos, cible) — CRM / formulaire / upload
 ↓ 2. Property DNA (style, gamme, cible, forces/faiblesses, élément wow, histoire, arguments)
 ↓ 3. Angle (coup de cœur · investissement · familial · luxe · quartier · avant/après · 3 points forts · visite express · expertise)
 ↓ 4. Script (Reel bien / Story / Avatar face cam / Post expert)
 ↓ 5. Plan de contenu (Hook→Promesse→3 arguments→projection→CTA ; ou cover→intro→pièces→point fort→localisation→CTA)
 ↓ 6. Génération visuelle (photo→camera move→frame-to-video · map→zoom géo · motion) — Kling / Runway / OpenArt
 ↓ 7. Avatar SI besoin (scripté, voix définie — PAS de live)
 ↓ 8. Assemblage (clips + avatar + textes écran + sous-titres + branding + CTA + musique)
 ↓ 9. Caption + CTA (légende · hashtags · version DM · commentaire épinglé · multicanal)
 ↓ 10. Export (Reel 9:16 · Story · TikTok · LinkedIn · Facebook · site · WhatsApp)
```
**Nom proposé** : **PROD'AI Content Factory** *(alt. : Attraction Engine · Real Estate Content Engine)*.
*Le détail éditorial existe déjà dans `05-MARQUE-ET-CONTENU/` (02-SYSTEME-EDITORIAL, 05-STYLE-SYSTEM-VIDEO-NEVA).*

---

## 6. Réconciliation marque & preuve
- **PROD'AI Lab** (fait pour vous) = les 3 couches + l'offre méta **Concept/Business 0→1**. **PROD'AI Academy** (apprendre) = former à n'importe quelle couche (surtout ATTRACT).
- **Séries animées → format premium d'ATTRACT** · **Luna Live Avatar → INTERACT** (les anciennes « signatures » se rangent dans les couches ; le label « signature/IP » reste un argument transverse).
- Discipline de preuve (cockpit §7) : chaque brique porte son **statut** (TESTÉ/PILOTE/HYPOTHÈSE) ci-dessus ; aucun prix/gain présenté comme acquis.

## ✅ À valider
1. Adopter le modèle **3 couches** comme colonne vertébrale du Lab ?
2. Les **4 briques** + **3 niveaux** — ok ?
3. Nom de la brique contenu : **PROD'AI Content Factory** ?

## ➡️ Ensuite
- [ ] Reporter cette structure dans le Miro (ajouter la couche ATTRACT) — *Miro à reconnecter.*
- [ ] Premier pilote mesurable = **Niveau 1 « contenu seul »** (cohérent avec l'ordre de travail du cockpit).
