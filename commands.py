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
                print(f"{colors.green}{droplet}:{colors.reset}")
                output = subprocess.run(f"ssh -o 'StrictHostKeyChecking no' {user}@{droplet} '{cmd}'", text=True, check=True, shell=True, capture_output=True)

                if verbose:
                    print(output.stdout)
        else:
            print(f"{colors.green}{droplet}:{colors.reset}")
            output = subprocess.run(f"ssh -o 'StrictHostKeyChecking no' {user}@{name} '{cmd}'", text=True, check=True, shell=True, capture_output=True)

            if verbose:
                print(output.stdout)

        print(f"{colors.green}done...{colors.reset}")

    except Exception as e:
        print(f"{colors.red}ERROR IN: commands: {e}{colors.reset}")
        sys.exit(1)

def commands_wordlist(api_key, verbose, user, name, cmd, wordlist):
    try:
        with open(wordlist, "r") as f:
            user_file = f.readlines()

        if '*' in name or ',' in name:
            droplets = list_all_droplets(api_key, name)

            c=0
            for word in user_file:
                cmd_fuzz = cmd.replace("FUZZ", word.strip())

                print(f"{colors.green}{droplets[c]}:{colors.reset}")
                output = subprocess.run(f"ssh -o 'StrictHostKeyChecking no' {user}@{droplets[c]} '{cmd_fuzz}'", text=True, check=True, shell=True, capture_output=True)
                print(output.stdout)

                if c >= len(droplets) - 1:
                    c=0
                else:
                    c+=1

        else:
            for word in user_file:
                cmd_fuzz = cmd.replace("FUZZ", word.strip())

                print(f"{colors.green}{name}:{colors.reset}")
                output = subprocess.run(f"ssh -o 'StrictHostKeyChecking no' {user}@{name} '{cmd_fuzz}'", text=True, check=True, shell=True, capture_output=True)
                print(output.stdout)


    except IndexError as e:
        pass
    except Exception as e:
        print(f"{colors.red}ERROR IN: commands_wordlist: {e}{colors.reset}")
