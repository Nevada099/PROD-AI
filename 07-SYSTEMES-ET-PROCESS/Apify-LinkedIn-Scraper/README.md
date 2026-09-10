# Scraper LinkedIn (Apify) — Mode d'emploi rapide

Ce script va chercher sur LinkedIn des profils (ex : directeurs d'agence immobilière) via l'Actor Apify [`harvestapi/linkedin-profile-search`](https://apify.com/harvestapi/linkedin-profile-search), et te sort un fichier CSV prêt à importer dans Lemlist, Apollo ou Google Sheets.

## 1. Installer les dépendances (une seule fois)

```bash
cd "Apify-LinkedIn-Scraper"
pip install -r requirements.txt
```

## 2. Renseigner ton token Apify

Récupère ton token sur [console.apify.com/account/integrations](https://console.apify.com/account/integrations).

Deux options (choisis-en une) :

**Option A — fichier `.env` (le plus simple)**
Crée un fichier `.env` dans ce dossier avec :
```
APIFY_API_TOKEN=ton_token_ici
```

**Option B — variable d'environnement**
```bash
export APIFY_API_TOKEN=ton_token_ici
```

⚠️ Ne partage jamais ce token et ne le colle pas dans un chat.

## 3. Régler la recherche

Ouvre `config.json` et modifie les critères sans toucher au code :

```json
{
  "profileScraperMode": "Full + email search",
  "searchQuery": "directeur agence immobilière",
  "locations": ["France"],
  "currentJobTitles": ["Directeur d'agence", "Responsable d'agence", "Director"],
  "profileLanguages": ["French"],
  "maxItems": 200
}
```

Champs utiles :
- `profileScraperMode` : `"Short"` (rapide, peu de données), `"Full"` (détaillé, sans email) ou `"Full + email search"` (détaillé + tentative de trouver l'email — le plus cher, ~0,01 $/profil).
- `searchQuery` : recherche floue (mots-clés libres).
- `locations` / `currentJobTitles` : listes, tu peux en ajouter/enlever autant que tu veux.
- `maxItems` : nombre max de profils. **Le nombre réel peut être bien inférieur** si peu de profils LinkedIn correspondent exactement aux critères (ex : 22 trouvés sur 200 demandés lors du premier test, car le croisement métier + titre exact + langue française est un filtre assez strict). Pour élargir : élargis `currentJobTitles`, enlève `profileLanguages`, ou simplifie `searchQuery`.

## 4. Lancer le scraping

```bash
python3 apify_linkedin_scraper.py
```

Le script :
1. lance l'Actor Apify avec les critères de `config.json` ;
2. attend la fin du run (vérifie le statut toutes les 10 secondes) ;
3. récupère les profils trouvés ;
4. exporte un CSV dans `output/` (ex : `output/linkedin_profiles_20260909-143000.csv`) ;
5. affiche dans le terminal : nombre de profils trouvés, temps écoulé, coût estimé.

## 5. Filtrer après coup (optionnel)

Pour ne garder que certains résultats sans relancer un scraping :

```bash
python3 apify_linkedin_scraper.py --filter-location "Paris" --filter-company "Orpi"
```

## Colonnes du CSV exporté

| Colonne | Description |
|---|---|
| fullName | Nom complet |
| headline | Titre LinkedIn |
| currentCompany | Entreprise actuelle |
| location | Ville / région |
| profileUrl | URL du profil LinkedIn |
| email | Email (si trouvé) |
| industry | ⚠️ toujours vide — cet Actor ne fournit pas ce champ |
| connectionDegree | ⚠️ toujours vide — cet Actor ne fournit pas ce champ |

Les colonnes `industry` et `connectionDegree` étaient prévues au départ, mais l'Actor réel ne les renvoie pas (il n'existe d'ailleurs pas d'Actor Apify `harvest_api/linkedin-profile-search-scraper` — le bon nom est `harvestapi/linkedin-profile-search`, corrigé lors du premier test). Elles restent dans le CSV (vides) pour ne pas casser un import déjà configuré dans Lemlist/Apollo.

## En cas d'erreur

Le script affiche un message clair dans le terminal si :
- le token est invalide ou expiré,
- le quota Apify est dépassé,
- le run prend plus de 30 minutes (timeout),
- une erreur réseau survient.

## Coût

Le prix dépend du nombre de profils et du plan Apify. Le script affiche le coût estimé du run à la fin (champ fourni par Apify). Vérifie aussi ton usage sur [console.apify.com/billing](https://console.apify.com/billing).
