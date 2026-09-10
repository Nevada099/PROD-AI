#!/usr/bin/env python3
"""Scraper LinkedIn via l'Actor Apify harvest_api/linkedin-profile-search-scraper."""

import csv
import json
import logging
import os
import sys
import time
from pathlib import Path

import requests

ACTOR_ID = "harvestapi~linkedin-profile-search"
BASE_URL = "https://api.apify.com/v2"
POLL_INTERVAL_SECONDS = 10
RUN_TIMEOUT_SECONDS = 30 * 60

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("apify_linkedin_scraper")


class ScraperError(RuntimeError):
    """Erreur non récupérable lors d'un échange avec l'API Apify."""


def load_token() -> str:
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        env_file = Path(__file__).parent / ".env"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                line = line.strip()
                if line.startswith("APIFY_API_TOKEN="):
                    token = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
    if not token:
        raise ScraperError(
            "APIFY_API_TOKEN manquant. Définis-le en variable d'environnement "
            "ou dans un fichier .env à la racine du projet (APIFY_API_TOKEN=...)."
        )
    return token


def load_config(config_path: str) -> dict:
    path = Path(config_path)
    if not path.exists():
        raise ScraperError(f"Fichier de config introuvable : {path}")
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def launch_scrape(token: str, params: dict) -> str:
    """Lance l'Actor Apify et retourne l'id du run."""
    url = f"{BASE_URL}/acts/{ACTOR_ID}/runs"
    log.info("Lancement de l'Actor Apify avec les paramètres : %s", params)
    response = requests.post(url, params={"token": token}, json=params, timeout=30)
    _raise_for_status(response, "lancement du run")
    run_id = response.json()["data"]["id"]
    log.info("Run lancé (id=%s)", run_id)
    return run_id


def wait_for_completion(
    token: str,
    run_id: str,
    poll_interval: int = POLL_INTERVAL_SECONDS,
    timeout: int = RUN_TIMEOUT_SECONDS,
) -> dict:
    """Poll le run toutes les `poll_interval` secondes jusqu'à SUCCEEDED (ou erreur/timeout)."""
    url = f"{BASE_URL}/actor-runs/{run_id}"
    start = time.monotonic()
    while True:
        elapsed = time.monotonic() - start
        if elapsed > timeout:
            raise ScraperError(f"Timeout ({timeout}s) dépassé en attendant la fin du run {run_id}.")

        response = requests.get(url, params={"token": token}, timeout=30)
        _raise_for_status(response, "suivi du run")
        run = response.json()["data"]
        status = run["status"]
        log.info("Statut du run : %s (%.0fs écoulées)", status, elapsed)

        if status == "SUCCEEDED":
            return run
        if status in ("FAILED", "ABORTED", "TIMED-OUT"):
            raise ScraperError(
                f"Le run Apify a échoué (statut={status}). "
                f"Détails : {run.get('statusMessage', 'aucun détail fourni')}"
            )
        time.sleep(poll_interval)


def get_results(token: str, run_id: str) -> list:
    """Récupère le dataset JSON produit par le run."""
    url = f"{BASE_URL}/actor-runs/{run_id}/dataset/items"
    response = requests.get(url, params={"token": token, "format": "json"}, timeout=60)
    _raise_for_status(response, "récupération des résultats")
    return response.json()


def filter_results(data: list, filters: dict) -> list:
    """Filtre une liste de profils : filters = {champ: sous-chaîne recherchée (insensible casse)}.

    Exemple : filter_results(data, {"location": "Paris", "industry": "Real Estate"})
    """
    if not filters:
        return data

    def matches(item: dict) -> bool:
        for field, expected in filters.items():
            value = str(item.get(field, "")).lower()
            if str(expected).lower() not in value:
                return False
        return True

    filtered = [item for item in data if matches(item)]
    log.info("Filtrage : %d/%d profils retenus (filtres=%s)", len(filtered), len(data), filters)
    return filtered


CSV_FIELDS = [
    "fullName", "headline", "currentCompany", "location",
    "profileUrl", "email", "industry", "connectionDegree",
]


def _flatten_profile(item: dict) -> dict:
    """Convertit un profil brut renvoyé par harvestapi/linkedin-profile-search
    vers les colonnes du cahier des charges. `industry` et `connectionDegree`
    ne sont pas fournis par cet Actor : laissés vides plutôt qu'inventés.
    """
    first = item.get("firstName") or ""
    last = item.get("lastName") or ""
    full_name = f"{first} {last}".strip() or item.get("publicIdentifier", "")

    current_positions = item.get("currentPosition") or []
    current_company = current_positions[0].get("companyName", "") if current_positions else ""

    location = item.get("location") or {}
    location_text = (location.get("parsed") or {}).get("text") or location.get("linkedinText") or ""

    emails = item.get("emails") or []
    first_email = emails[0] if emails else {}
    email = first_email.get("email", "") if isinstance(first_email, dict) else str(first_email)

    return {
        "fullName": full_name,
        "headline": item.get("headline", ""),
        "currentCompany": current_company,
        "location": location_text,
        "profileUrl": item.get("linkedinUrl", ""),
        "email": email,
        "industry": "",
        "connectionDegree": "",
    }


def export_csv(data: list, filename: str) -> None:
    """Exporte les résultats en CSV, colonnes fixes, compatible Lemlist/Apollo/Google Sheets."""
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    log.info("CSV exporté : %s (%d lignes)", path, len(data))


def _raise_for_status(response: requests.Response, action: str) -> None:
    if response.status_code == 401:
        raise ScraperError(f"Token Apify invalide ou expiré (401) lors de : {action}.")
    if response.status_code == 402:
        raise ScraperError(f"Quota Apify dépassé (402) lors de : {action}.")
    if response.status_code == 404:
        raise ScraperError(f"Ressource introuvable (404) lors de : {action}. Vérifie l'ID de l'Actor/du run.")
    if not response.ok:
        raise ScraperError(
            f"Erreur Apify ({response.status_code}) lors de : {action}. Réponse : {response.text[:500]}"
        )


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Lance le scraper LinkedIn via Apify et exporte un CSV.")
    parser.add_argument("--config", default="config.json", help="Chemin du fichier de config (défaut: config.json)")
    parser.add_argument("--output-dir", default="output", help="Dossier de sortie des CSV (défaut: output)")
    parser.add_argument("--filter-location", default=None, help="Filtre post-scraping sur la localisation")
    parser.add_argument("--filter-company", default=None, help="Filtre post-scraping sur l'entreprise actuelle")
    args = parser.parse_args()

    try:
        token = load_token()
        config = load_config(args.config)

        run_id = launch_scrape(token, config)
        run = wait_for_completion(token, run_id)

        raw_data = get_results(token, run_id)
        log.info("%d profils récupérés.", len(raw_data))
        data = [_flatten_profile(item) for item in raw_data]

        filters = {}
        if args.filter_location:
            filters["location"] = args.filter_location
        if args.filter_company:
            filters["currentCompany"] = args.filter_company
        if filters:
            data = filter_results(data, filters)

        timestamp = time.strftime("%Y%m%d-%H%M%S")
        output_path = Path(args.output_dir) / f"linkedin_profiles_{timestamp}.csv"
        export_csv(data, str(output_path))

        cost = run.get("usageTotalUsd")
        elapsed = run.get("stats", {}).get("runTimeSecs")
        log.info(
            "Terminé — %d profils exportés | temps d'exécution: %s | coût estimé: %s",
            len(data),
            f"{elapsed:.0f}s" if elapsed is not None else "inconnu",
            f"${cost:.4f}" if cost is not None else "inconnu",
        )
        return 0

    except ScraperError as exc:
        log.error(str(exc))
        return 1
    except requests.RequestException as exc:
        log.error("Erreur réseau : %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
