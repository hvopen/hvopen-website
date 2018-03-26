#!/bin/bash

set -e

HOW_MANY=${1:-1}

FILES=$(git diff-tree --no-commit-id -r --name-only HEAD HEAD~${HOW_MANY} | grep ^_events | sort | uniq)

for f in ${FILES}; do
    if [[ -e "$f" ]]; then
        echo "Syncing $f to meetup"
        ./meetup-sync.py $f
    fi
done
