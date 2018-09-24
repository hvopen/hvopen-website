#!/bin/bash

set -e

HOW_MANY=${1:-1}

FILES=$(git diff-tree --no-commit-id -r --name-only HEAD HEAD~${HOW_MANY} | grep ^_events | sort | uniq)

if [[ ! -d .venv3 ]]; then
    virtualenv -p python3 .venv3
    source .venv3/bin/activate
else
    source .venv3/bin/activate
fi

pip install -U hvopen_tools

for f in ${FILES}; do
    if [[ -e "$f" ]]; then
        echo "Syncing $f to meetup"
        meetup-sync $f
    fi
done
