#!/bin/bash

set -eux

DATE=$1
REGEX="^[0-9]{4}-[0-9]{2}-[0-9]{2}$"


if [[ ! ( "${DATE}" =~ ${REGEX} ) ]]; then
    echo "Failed to regex match"
    exit 1
fi

YEAR=$(echo ${DATE} | cut -c 1-4)

FILE="_events/${YEAR}/${DATE}-lunch.md"

if [[ -e ${FILE} ]]; then
    echo "File: ${FILE} already exists!"
    exit 1
fi

cat - <<EOF > ${FILE}
---
dtend: ${DATE} 13:00:00 -0400
dtstart: ${DATE} 12:00:00 -0400
location: Mole Mole
title: HV Open Lunch
type: lunch
---

Interested in talking more about Open Technology? Once a month we get
together for an informal lunch to talk tech, and catch up between
meetings. This is open to anyone.

Bring your ideas, open source questions, and grab some good food at
the same time!

EOF

echo "Wrote ${FILE}. Run ./meetup-sync.py ${FILE} to register it on meetup"
