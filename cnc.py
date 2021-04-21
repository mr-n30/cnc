#!/usr/bin/env python3
import sys
import json
import yaml
import requests
import argparse
from colors import *
from commands import *
from digitalocean import *

# Parse command line arguments
parser = argparse.ArgumentParser(description="Command aNd Control multiple servers")
parser.add_argument("mode", help="Options are: config, cmd, wordlist, upload, download")
parser.add_argument("-C", "--cmd", help="Command(s) to run on droplets")
parser.add_argument("-u", "--user", help="Username on the droplet running the command(s) on")
parser.add_argument("-n", "--name", help="Name of the droplet running the command(s) on e.g droplet* or droplet1,droplet2,...")
parser.add_argument("-c", "--config", required=True, help="Path to your config.yaml file containing your API key")
parser.add_argument("-v", "--verbose", action="store_true", help="If enabled command output will be printed to the terminal")
parser.add_argument("-w", "--wordlist", help="Name of the droplet running the command(s) on e.g droplet* or droplet1,droplet2,...")

args     = parser.parse_args()
cmd      = args.cmd
mode     = args.mode
user     = args.user
name     = args.name
config   = args.config
verbose  = args.verbose
wordlist = args.wordlist

def main():
    try:
        # Get digitalocean api key
        with open(config, 'r') as f:
            yaml_data = yaml.safe_load(f)

        api_key = yaml_data["digitalocean"][0]

        # Mode: config
        if mode == "config":
            if config:
                droplet_name = input(f"{colors.yellow}Enter the name you want for the droplet(s):{colors.reset} ")
                digitalocean(api_key)
                etc_hosts(api_key, droplet_name)

        # Mode: cmd
        elif mode == "cmd":
            if config and cmd and user and name:
                if not verbose:
                    commands(api_key, 0, user, name, cmd)
                else:
                    commands(api_key, verbose, user, name, cmd)
            else:
                print(f"{colors.red}Missing one or more of the following arguments: --cmd|--user|--name{colors.reset}")
                sys.exit(1)

        # Mode: wordlist
        elif mode == "wordlist":
            if config and cmd and user and name and wordlist:
                if not verbose:
                    commands_wordlist(api_key, 0, user, name, cmd, wordlist)
                else:
                    commands_wordlist(api_key, verbose, user, name, cmd, wordlist)
            else:
                print(f"{colors.red}Missing one or more of the following arguments: --cmd|--user|--name|--wordlist{colors.reset}")
                sys.exit(1)

    except KeyboardInterrupt as e:
        print("")
        print(f"{colors.green}cancelling...{colors.reset}")
        print("")
        sys.exit()
    except Exception as e:
        print(f"{colors.red}ERROR IN: main: {e}{colors.reset}")
        sys.exit(1)

if __name__ == "__main__":
    main()
