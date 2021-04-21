#!/usr/bin/env python3
import json
import requests

def list_all_droplets(api_key, name):
    try:
        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        r = requests.get("https://api.digitalocean.com/v2/droplets", headers=headers)

        json_data = json.loads(r.text)

        if '*' in name:
            droplets = []

            for droplet_name in json_data["droplets"]:
                if name.strip('*') in droplet_name["name"]:
                    droplets.append(droplet_name["name"])

            return droplets

        elif ',' in name:
            droplets = name.split(',')

            return droplets

        else:
            print(f"{colors.red}Droplet name not found: {name}{colors.reset}")
            sys.exit(1)

    except Exception as e:
        print(f"{colors.red}ERROR IN: list_all_droplets: {e}{colors.reset}")
