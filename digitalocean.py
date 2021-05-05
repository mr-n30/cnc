#!/usr/bin/env python3
import sys
from colors import *
from etc_hosts import *
from create_droplets import *
from list_available_sizes import *
from list_available_distribution_images import *

def digitalocean(api_key, name):
    try:
        # List available images
        print(f"{colors.yellow}Listing available distributions and regions:{colors.reset}")
        list_available_distribution_images(api_key)

        distribution = input(f"{colors.yellow}Enter a distribution:{colors.reset} ")
        print(f"You selected: {distribution}")

        region = input(f"{colors.yellow}Enter a region:{colors.reset} ")
        print(f"You selected: {region}")

        amount = input(f"{colors.yellow}Enter how many images to create:{colors.reset} ")
        print(f"You entered: {amount}")

        # List available sizes
        print(f"{colors.yellow}Listing available sizes for:{colors.reset} {distribution}")
        list_available_sizes(api_key, region)

        size = input(f"{colors.yellow}Enter the size of droplet you would like to create:{colors.reset} ")
        print(f"You entered: {size}")

        # Create droplet(s)
        create_droplets(api_key, amount, name, region, size, distribution)

    except KeyboardInterrupt as e:
        print("")
        print(f"{colors.green}Cancelling...{colors.reset}")
        print("")
        sys.exit()
