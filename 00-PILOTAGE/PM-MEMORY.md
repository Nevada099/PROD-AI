# 🧠 PM-MEMORY — Mémoire de travail du Business Dev PM

*Réécrit à jour par l'agent `business-dev-pm` à la fin de chaque session. Ne pas éditer à la main (sauf correction volontaire).*

*Dernière session PM : 2026-07-09*

## Dernière activité constatée par agent

| Agent | Dernière activité | Source |
|---|---|---|
| market-research | **Aucune** — jamais activé, aucun livrable produit | Seulement la fiche `RH/Agent-Market-Research.md` ; aucun fichier de travail |
| offer-strategy | 2026-07-07 (initialisation seule) | `OFFER_HISTORY.md` — 1 seule entrée « ожидает ввода », offre non fixée |
| content-marketing | 2026-07-08 | `Veille Tendances/SOURCES.md` + `Veille-2026-07.md` (probablement routine auto de veille, pas session manuelle) |
| ai-systems-architect | 2026-07-08 / 09 (très actif) | `Automatisations/` : JobsAI Marche 1 en prod, Appartments en attente validation |

## Structure constatée

- Le dossier `Business Dev/` est **plat** : pas de sous-dossier par agent. Il n'existe PAS de fichiers Session Log / Next Actions / Project Memory dédiés par agent.
- Sources réelles d'activité : `SESSION-LOG.md` (journal global), `OFFER_HISTORY.md` (offer-strategy), `Veille Tendances/` (content-marketing), `Automatisations/` (ai-systems-architect).
- market-research n'a AUCUNE trace d'activité nulle part.

## Dépendances déjà signalées

| Date signalée | Dépendance | Statut |
|---|---|---|
| 2026-07-09 | offer-strategy ne peut pas fixer l'offre : aucun SWOT / analyse concurrentielle de market-research n'existe (dépendance structurelle imposée par sa fiche) | **EN ATTENTE** — bloquant racine |
| 2026-07-09 | content-marketing produit de la veille et propose du contenu (cas PROD'AI, coaching IA daté) sans offre/positionnement/prix stabilisés par offer-strategy | **EN ATTENTE** — risque de contenu sur base instable |
| 2026-07-09 | ai-systems-architect : travaille sur automatisations internes (JobsAI, Appartments), non liées à la structure produit → pas de conflit actif avec offer-strategy pour l'instant | Surveillé, non bloquant |

## Décisions Katerina en attente (blocages hors-agents)

- Appartments : choisir 1 des 3 variantes + autoriser le credential Google Drive/Sheets dans n8n
- JobsAI : faire les tests réels de la Marche 1 (vraie alerte, clics ✅/❌)
- Valider `Profil-Candidature.md`
- Valider les 3 nouvelles sources de veille proposées le 08.07

## Notes

- Première session PM effectuée le 2026-07-09 : état des lieux en lecture seule, aucun agent lancé.
