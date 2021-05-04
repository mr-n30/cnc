#!/usr/bin/env python3
import sys
import subprocess
from colors import *
from list_all_droplets import *

def upload(api_key, user, name, destination, data):
    try:
        # Run command(s) on all droplets
        if name == '*':
            droplets = list_all_droplets(api_key, name)

            for droplet in droplets:
                print(f"{colors.green}{droplet}:{colors.reset}")
                output = subprocess.run(f"scp -r {data} {user}@{droplet}:{destination}", text=True, check=True, shell=True, capture_output=True)
                print(output.stdout)

        # Run command(s) on certain droplets
        elif '*' in name or ',' in name:
            droplets = list_all_droplets(api_key, name)

            for droplet in droplets:
                print(f"{colors.green}{droplet}:{colors.reset}")
                output = subprocess.run(f"scp -r {data} {user}@{droplet}:{destination}", text=True, check=True, shell=True, capture_output=True)
                print(output.stdout)

        # Run command(s) on a single droplet
        else:
            print(f"{colors.green}{name}:{colors.reset}")
            output = subprocess.run(f"scp -r {data} {user}@{droplet}:{destination}", text=True, check=True, shell=True, capture_output=True)
            print(output.stdout)

        print(f"{colors.green}done...{colors.reset}")

    # Errors
    except Exception as e:
        print(f"{colors.red}ERROR IN: upload: {e}{colors.reset}")
        sys.exit(1)

