#!/usr/bin/env python3

import argparse
import os
import sys
from urllib.request import urlopen, URLError, HTTPError

def download_authorized_keys(username):
    # Define the URL with the provided username
    authorized_keys_url = f"https://github.com/{username}.keys"

    # Create the ~/.ssh/ directory if it doesn't exist
    os.makedirs(os.path.expanduser('~/.ssh/'), exist_ok=True)

    try:
        # Use urlopen to download the file
        with urlopen(authorized_keys_url) as response:
            # Append the contents to authorized_keys
            with open(os.path.expanduser('~/.ssh/authorized_keys'), 'a') as auth_keys_file:
                auth_keys_file.write(response.read().decode('utf-8'))

            print("Authorized keys successfully downloaded and appended.")
            sys.exit(0)  # Exit with success code
    except HTTPError as e:
        print(f"HTTP Error {e.code}: Unable to download authorized keys.")
        sys.exit(1)  # Exit with failure code
    except URLError as e:
        print(f"URL Error: Unable to reach the server. {e.reason}")
        sys.exit(1)  # Exit with failure code

def main():
    parser = argparse.ArgumentParser(description='Download and append authorized_keys file.')
    parser.add_argument('-u', '--username', help='Specify the username', required=False)

    args = parser.parse_args()

    # If the username is not provided as a command-line argument, prompt the user
    if not args.username:
        username = input("Enter your name: ")

        # Validate that the username is not empty
        if not username:
            print("Error: Username cannot be empty.")
            sys.exit(1)  # Exit with failure code
    else:
        username = args.username

    download_authorized_keys(username)

if __name__ == "__main__":
    main()
