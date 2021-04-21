#!/usr/bin/env python3
import json
import yaml
import requests
import argparse
from commands import *
from digitalocean import *

# Parse command line arguments
parser = argparse.ArgumentParser(description="Command aNd Control multiple servers")
parser.add_argument("-c", "--config", required=True, help="Path to your config.yaml file containing your API key")
parser.add_argument("-C", "--cmd", help="Command(s) to run on droplets")
parser.add_argument("-u", "--user", help="Username on the droplet running the command(s) on")
parser.add_argument("-n", "--name", help="Name of the droplet running the command(s) on")
parser.add_argument("-v", "--verbose", help="If enabled command output will be printed to the terminal")

args    = parser.parse_args()
cmd     = args.cmd
user    = args.user
config  = args.config
verbose = args.verbose

def main():
    # Get digitalocean api key
    with open(config, 'r') as f:
        yaml_data = yaml.safe_load(f)

    api_key = yaml_data["digitalocean"][0]

    # digitalocean
    if config:
        digitalocean(api_key)

    # Run commands on droplets
    if config and cmd and user:
        if not verbose:
            commands(api_key, 0, user, name, cmd)
        else:
            commands(api_key, verbose, user, name, cmd)

if __name__ == "__main__":
    main()
