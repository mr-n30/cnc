#!/usr/bin/env python3
import sys
import json
import requests
from colors import *

def create_droplets(api_key, amount, name, region, size, image):
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        # SSH public key
        ssh_choice = input(f"{colors.yellow}Do you want to create a new SSH public key? (y/n){colors.reset} ")

        if ssh_choice.lower() == 'y':
            # Create SSH public key
            ssh_creation = requests.post("https://api.digitalocean.com/v2/account/keys", headers=headers, json={
                "name": "CNC SSH KEY",
                "public_key": ssh_key
            })

            ssh_json_data = json.loads(ssh_creation.text)

            ssh_id = ssh_json_data["ssh_key"]["id"]
        else:
            # Retrieve SSH public key
            ssh_creation = requests.get("https://api.digitalocean.com/v2/account/keys", headers=headers)

            ssh_json_data = json.loads(ssh_creation.text)

            for i in ssh_json_data["ssh_keys"]:
                print(f"ID:{i['id']} - {i['name']}")

            ssh_id = input(f"{colors.yellow}Enter the ID value of the SSH key you'd like to use:{colors.reset} ")
            print(f"You entered: {ssh_id}")

        if int(amount) <= 1:
            request_body = {
                "name": name,
                "region": region,
                "size": size,
                "image": image,
                "ssh_keys": [
                    int(ssh_id)
                ],
                "backups": "false",
                "ipv6": "false",
                "private_networking": "true",
                "tags": [
                    "cnc"
                ]
            }

        elif int(amount) > 1:
            names = []
            [names.append(f"{name}{c}") for c in range(int(amount))]

            request_body = {
                "names": names,
                "region": region,
                "size": size,
                "image": image,
                "ssh_keys": [
                    int(ssh_id)
                ],
                "backups": "false",
                "ipv6": "false",
                "private_networking": "false",
                "tags": [
                    "cnc"
                ]
            }

        else:
            print(f"{colors.red}Seriously...{colors.reset}")
            sys.exit(1)

        print(f"{colors.green}creating droplet(s)...{colors.reset}")

        r = requests.post("https://api.digitalocean.com/v2/droplets", headers=headers, json=request_body)
        print(r.text)

        print(f"{colors.green}done...{colors.reset}")

    except Exception as e:
        print(f"{colors.red}ERROR IN: create_droplets: {e}{colors.reset}")
        sys.exit(1)
