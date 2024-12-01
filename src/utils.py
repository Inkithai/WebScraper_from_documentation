import requests
from bs4 import BeautifulSoup
import json
import os


def fetch_html(url, headers):
    """Fetch HTML content from a URL."""
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def save_to_json(data, filepath):
    """Save data to a JSON file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Saved data to {filepath}")
