#!/usr/bin/env python3
import sys
import json
import requests
from colors import *

def etc_hosts(api_key, name):
    try:
        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        r = requests.get("https://api.digitalocean.com/v2/droplets", headers=headers)

        json_data = json.loads(r.text)


        with open("/etc/hosts", "a") as f:
            f.write("\n\n\n# CNC DATA BELOW\n")

            for droplet in json_data["droplets"]:
                if name in droplet["name"]:
                    print(f"{droplet['networks']['v4'][1]['ip_address']}\t{droplet['name']}")
                    f.write(f"{droplet['networks']['v4'][1]['ip_address']}\t{droplet['name']}\n")

    except IndexError as e:
        pass
    except Exception as e:
        print(f"{colors.red}ERROR IN: etc_hosts: {e}{colors.reset}")
        sys.exit(1)
