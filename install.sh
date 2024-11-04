#!/bin/bash

# Automated Install Script
# This script will update the system and install common packages

echo "Starting the installation process..."

# Update the package list
sudo apt update
echo "Package list updated."

# Upgrade installed packages
sudo apt upgrade -y
echo "Installed packages upgraded."

# Install necessary packages
PACKAGES=(
    git
    python3
    python3-pip
    python3-venv
    curl
    build-essential
)

echo "Installing packages..."
for package in "${PACKAGES[@]}"; do
    sudo apt install -y "$package"
    echo "$package installed."
done

# Create a Python virtual environment
echo "Creating a Python virtual environment..."
python3 -m venv myenv
echo "Virtual environment 'myenv' created."

# Activate the virtual environment
echo "To activate the virtual environment, run:"
echo "source myenv/bin/activate"

echo "Installation process completed."
