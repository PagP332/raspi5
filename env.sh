#!/bin/bash

# Navigate to the target directory
cd ~/Desktop/PD/raspi5 || { echo "Directory not found!"; exit 1; }

# Activate the Python virtual environment
source env/bin/activate

python3 scripts/main.py
