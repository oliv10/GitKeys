#!/bin/bash

# Function to display usage information
usage() {
    echo "Usage: $0 [-u <username>]"
    exit 1
}

# Parse command-line options
while getopts "u:" opt; do
    case $opt in
        u)
            USERNAME="$OPTARG"
            ;;
        \?)
            usage
            ;;
    esac
done

# If the username is not provided as a flag, prompt the user
if [ -z "$USERNAME" ]; then
    read -p "Enter your name: " USERNAME

    # Validate that the username is not empty
    if [ -z "$USERNAME" ]; then
        echo "Error: Username cannot be empty."
        exit 1
    fi
fi

# Define the URL with the provided username
AUTHORIZED_KEYS_URL="https://github.com/$USERNAME.keys"

# Create the ~/.ssh/ directory if it doesn't exist
mkdir -p ~/.ssh/

# Use curl to download the file and append its contents to authorized_keys
curl -s "$AUTHORIZED_KEYS_URL" >> ~/.ssh/authorized_keys

# Check if curl was successful
if [ $? -eq 0 ]; then
    echo "Authorized keys successfully downloaded and appended."
    exit 0  # Exit with success code
else
    echo "Error: Unable to download authorized keys."
    exit 1  # Exit with failure code
fi
