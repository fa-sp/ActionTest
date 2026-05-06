import requests
import json
from datetime import datetime
from pathlib import Path

BASE_URL = "https://jsonapi.org"
ENDPOINT = "/articles"

PARAMS = {
    "include": "author",
    "fields[articles]": "title,body,author",
    "fields[people]": "name",
}

OUTPUT_DIR = Path("data")
OUTPUT_DIR.mkdir(exist_ok=True)

def fetch_data():
    url = f"{BASE_URL}{ENDPOINT}"
    response = requests.get(url, params=PARAMS, timeout=30)
    response.raise_for_status()
    return response.json()

def save_data(data):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H")
    file_path = OUTPUT_DIR / f"{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Saved data to {file_path}")

def main():
    data = fetch_data()
    save_data(data)

if __name__ == "__main__":
    main()
