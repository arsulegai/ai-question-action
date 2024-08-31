#!/bin/bash

# Get user input from the command line arguments
USER_INPUT="$1"

echo "Processing user input: $USER_INPUT"

python3 query-runner.py "$USER_INPUT"
