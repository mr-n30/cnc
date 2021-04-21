#!/usr/bin/env python3
import json
import requests
from colors import *

def list_available_distribution_images(api_key):
    try:
        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        r = requests.get("https://api.digitalocean.com/v2/images?type=distribution", headers=headers)

        json_data = json.loads(r.text)

        for image in json_data["images"]:
            print(f"{colors.inverted}{image['slug']}{colors.reset}")

            if image["status"] == "available":
                print(image["regions"])

            print("")

    except Exception as e:
        print(f"ERROR in: list_available_images: {e}")
