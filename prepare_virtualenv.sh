#!/usr/bin/env sh

! [ -d venv ] && virtualenv -p python3 venv || echo "venv already exists"

printf "%s\n\n%s\n\n%s\n\n%s\n\n" '1. run' 'source venv/bin/activate' '2. verify python3 with' 'python --version'
printf "%s\n\n%s\n\n" '3. then run' 'python -m pip install -r requirements.txt'
