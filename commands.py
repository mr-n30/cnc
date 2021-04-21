#!/usr/bin/env python3
import sys
import subprocess
from colors import *
from list_all_droplets import *

def commands(api_key, verbose, user, name, cmd):
    try:
        if '*' in name or ',' in name:
            droplets = list_all_droplets(api_key, name)

            for droplet in droplets:
                output = subprocess.run(f"ssh {user}@{droplet} '{cmd}'", shell=True, capture_output=True)

                if verbose:
                    print(output.stdout)
        else:
            output = subprocess.run(f"ssh {user}@{droplet} '{cmd}'", shell=True, capture_output=True)
            if verbose:
                print(output.stdout)

        print(f"{colors.green}done...{colors.reset}")

    except Exception as e:
        print(f"{colors.red}ERROR IN: commands: {e}")
        sys.exit(1)
