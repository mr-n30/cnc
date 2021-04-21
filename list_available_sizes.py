#!/usr/bin/env python3
import json
import requests
from colors import *

def list_available_sizes(api_key, region):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    r = requests.get("https://api.digitalocean.com/v2/regions", headers=headers)

    json_data = json.loads(r.text)

    for size in json_data["regions"]:
        if size["slug"] == region:
            print(size["sizes"])
            break
