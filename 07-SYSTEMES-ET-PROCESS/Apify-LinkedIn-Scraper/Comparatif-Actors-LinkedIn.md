# Comparatif des Actors Apify pour scraper LinkedIn (09/09/2026)

Sources : recherche directe dans le Store Apify (`search-actors` / `fetch-actor-details`) + 2 guides externes cités par Katerina ([use-apify.com/blog/linkedin-scraper-tutorial-2026](https://use-apify.com/blog/linkedin-scraper-tutorial-2026), [use-apify.com/docs/best-apify-actors/best-linkedin-scrapers](https://use-apify.com/docs/best-apify-actors/best-linkedin-scrapers)).

## Tableau comparatif

| Actor | Meilleur pour | Prix | Filtres disponibles | Points forts | Limites / risques |
|---|---|---|---|---|---|
| **[harvestapi/linkedin-profile-search](https://apify.com/harvestapi/linkedin-profile-search)** ⭐ testé | Recherche floue large (poste + secteur + ville), pas de liste de cibles connue | $0,002–0,004/profil (Short/Full) · $0,01/profil (Full + email) | Riches : `searchQuery`, `locations`, `currentJobTitles`, `industryIds`/`functionIds`, `seniorityLevelIds`, `companyHeadcount`, `profileLanguages`, années d'expérience… | Sans cookies (posture légale plus sûre — cf. guide). 42 042 utilisateurs, note 4,39/5. **Testé en réel le 09/09 : 22 profils pour 0,29 $.** | Le nombre réel de résultats peut être très inférieur au `maxItems` demandé si les critères combinés sont trop stricts. Ne renvoie pas de champ `industry` ni `connectionDegree` en sortie. |
| **[harvestapi/linkedin-profile-search-by-name](https://apify.com/harvestapi/linkedin-profile-search-by-name)** | Recherche par nom déjà identifié (export CRM, salon, event) | $0,002–0,01/profil | Nom + mêmes filtres secondaires que ci-dessus | Complément dédié, plus précis qu'une recherche floue sur un nom | Peu pertinent pour prospection large (il faut déjà avoir les noms) |
| **[harvestapi/linkedin-company-search](https://apify.com/harvestapi/linkedin-company-search)** | Étape 1 d'une prospection par réseau/franchise (trouver les pages entreprises LinkedIn) | $0,002–0,004/résultat | `locations`, `industryIds`, `companySize` | Rapide pour lister les entités d'un secteur (ex : franchises immobilières) | Ne donne que les entreprises, pas les profils — à combiner avec l'Actor suivant |
| **[harvestapi/linkedin-company-employees](https://apify.com/harvestapi/linkedin-company-employees)** | Cibler **tous** les employés d'une entreprise/franchise connue, filtrés par poste | $0,003–0,012/profil | `companies` (URLs), `jobTitles`, `seniorityLevelIds`, `companyHeadcount`… | Le plus exhaustif pour une prospection par réseau identifié (ex : tous les directeurs d'agence Orpi). 26 827 utilisateurs, note 4,6/5 | Nécessite d'avoir les URLs LinkedIn des entreprises en amont → combo avec `linkedin-company-search` |
| **[apimaestro/linkedin-profile-search-scraper](https://apify.com/apimaestro/linkedin-profile-search-scraper)** | Recherche simple (nom/poste/ville), budget serré, test rapide | $0,005/profil (flat, email optionnel inclus) | `firstname`, `lastname`, `location`, `current_job_title`, `include_email` (bool) | Simple, moins cher que le mode email de HarvestAPI | Seulement 3 avis (peu de recul), pas de filtre secteur/taille entreprise/ancienneté — à valider sur petit volume avant de scaler |

## Framework de décision

1. **Poste générique + secteur, pas de cibles connues** (ex : « directeurs d'agence immobilière en France ») → `harvestapi/linkedin-profile-search`. C'est l'Actor déjà branché dans `apify_linkedin_scraper.py`.
2. **Réseaux/franchises identifiés** (Orpi, Century 21, Laforêt, Guy Hoquet, iad, Safti, Stéphane Plaza, Efficity…) → combo `harvestapi/linkedin-company-search` (trouver les pages entreprises) **puis** `harvestapi/linkedin-company-employees` filtré par poste. Plus exhaustif qu'une recherche floue.
3. **Liste de noms déjà en main** → `harvestapi/linkedin-profile-search-by-name`.
4. **Budget minimal / test rapide, critères simples** → `apimaestro/linkedin-profile-search-scraper`, en validant sur un petit volume avant de scaler (peu d'avis disponibles).

## Bonnes pratiques retenues des 2 guides externes

- **Actors sans cookies préférés** : demander le cookie de session LinkedIn à l'utilisateur revient à lui faire enfreindre les conditions d'utilisation LinkedIn en son nom propre — HarvestAPI et ApiMaestro n'en demandent pas.
- **Commencer petit** : tester sur 20-50 profils avant de lancer un run à 200+.
- **Taux de match email limité** : 20-60 % selon les guides — ne pas s'attendre à un email pour chaque profil (confirmé par le test réel : sur 22 profils, une partie seulement avait un email).
- **RGPD** : pour des données de résidents UE, il faut une base légale, de la transparence sur l'usage, et des délais de conservation définis — à garder en tête avant tout envoi en masse vers Lemlist/Apollo.
- **Vérifier les emails avant envoi en masse** : ne pas exploiter des emails devinés/non validés sans étape de vérification.

## Sauvegarde

Ce tableau : `Prod'AI/07-SYSTEMES-ET-PROCESS/Apify-LinkedIn-Scraper/Comparatif-Actors-LinkedIn.md`
Version condensée reprise dans le skill : `~/.claude/skills/apify-linkedin-scraping/SKILL.md`
